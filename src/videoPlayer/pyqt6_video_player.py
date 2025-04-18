# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations

import gc

from src.videoPlayer.SeekBar import SeekBar
from src.videoPlayer.VolumeSlider import VolumeSlider

"""PySide6 Multimedia player example"""

import sys
from PySide6.QtCore import QStandardPaths, Qt, Slot
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog,
                               QMainWindow, QSlider, QStyle, QToolBar, QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy)
from PySide6.QtMultimedia import (QAudioOutput, QMediaFormat,
                                  QMediaPlayer, QAudio)
from PySide6.QtMultimediaWidgets import QVideoWidget

AVI = "video/x-msvideo"  # AVI

MP4 = 'video/mp4'


def get_supported_mime_types():
    result = []
    for f in QMediaFormat().supportedFileFormats(QMediaFormat.Decode):
        mime_type = QMediaFormat(f).mimeType()
        result.append(mime_type.name())
    return result


class VideoPlayerWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self._playlist = []  # FIXME 6.3: Replace by QMediaPlaylist?
        self._playlist_index = -1
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)

        self._player.errorOccurred.connect(self._player_error)

        seek_bar_tool_bar = QToolBar()
        self.addToolBar(Qt.ToolBarArea.BottomToolBarArea, seek_bar_tool_bar)
        self.addToolBarBreak(Qt.ToolBarArea.BottomToolBarArea)

        self._seek_bar = SeekBar(self._player)
        seek_bar_tool_bar.addWidget(self._seek_bar)
        tool_bar = QToolBar()
        self.addToolBar(Qt.ToolBarArea.BottomToolBarArea, tool_bar)
        tool_bar_lower_widget = QWidget()
        tool_bar.addWidget(tool_bar_lower_widget)

        file_menu = self.menuBar().addMenu("&File")
        icon = QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen)
        open_action = QAction(icon, "&Open...", self, shortcut=QKeySequence.Open, triggered=self.open)
        file_menu.addAction(open_action)
        tool_bar.addAction(open_action)
        icon = QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit)
        exit_action = QAction(icon, "E&xit", self, shortcut="Ctrl+Q", triggered=self.close)
        file_menu.addAction(exit_action)

        play_menu = self.menuBar().addMenu("&Play")
        style = self.style()
        icon = QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart,
                               style.standardIcon(QStyle.SP_MediaPlay))
        self._play_action = tool_bar.addAction(icon, "Play")
        self._play_action.triggered.connect(self.playPauseClicked)
        play_menu.addAction(self._play_action)

        icon = QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipBackward,
                               style.standardIcon(QStyle.SP_MediaSkipBackward))
        self._previous_action = tool_bar.addAction(icon, "Previous")
        self._previous_action.triggered.connect(self.previous_clicked)
        play_menu.addAction(self._previous_action)

        # icon = QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause,
        #                        style.standardIcon(QStyle.SP_MediaPause))
        # self._pause_action = toolbar_lower.addAction(icon, "Pause")
        # self._pause_action.triggered.connect(self._player.pause)
        # play_menu.addAction(self._pause_action)

        icon = QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipForward,
                               style.standardIcon(QStyle.SP_MediaSkipForward))
        self._next_action = tool_bar.addAction(icon, "Next")
        self._next_action.triggered.connect(self.next_clicked)
        play_menu.addAction(self._next_action)

        icon = QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop,
                               style.standardIcon(QStyle.SP_MediaStop))
        self._stop_action = tool_bar.addAction(icon, "Stop")
        self._stop_action.triggered.connect(self._ensure_stopped)
        play_menu.addAction(self._stop_action)
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tool_bar.addWidget(spacer)
        self._volume_slider = VolumeSlider(self._audio_output)
        tool_bar.addWidget(self._volume_slider)

        icon = QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout)
        about_menu = self.menuBar().addMenu("&About")
        about_qt_act = QAction(icon, "About &Qt", self, triggered=qApp.aboutQt)  # noqa: F821
        about_menu.addAction(about_qt_act)

        self._video_widget = QVideoWidget()
        self.setCentralWidget(self._video_widget)
        self._player.playbackStateChanged.connect(self.update_buttons)
        self._player.setVideoOutput(self._video_widget)

        self.update_buttons(self._player.playbackState())
        self._mime_types = []

    def closeEvent(self, event):
        self._ensure_stopped()
        event.accept()

    def seek_position(self, position):
        if self._player.mediaStatus() in [QMediaPlayer.NoMedia, QMediaPlayer.InvalidMedia]:
            self.open()
        self._player.setPosition(position)

    @Slot()
    def open(self):
        self._ensure_stopped()
        file_dialog = QFileDialog(self)

        is_windows = sys.platform == 'win32'
        if not self._mime_types:
            self._mime_types = get_supported_mime_types()
            if is_windows and AVI not in self._mime_types:
                self._mime_types.append(AVI)
            elif MP4 not in self._mime_types:
                self._mime_types.append(MP4)

        file_dialog.setMimeTypeFilters(self._mime_types)

        default_mimetype = MP4
        if default_mimetype in self._mime_types:
            file_dialog.selectMimeTypeFilter(default_mimetype)

        movies_location = QStandardPaths.writableLocation(QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movies_location)
        if file_dialog.exec() == QDialog.Accepted:
            url = file_dialog.selectedUrls()[0]
            self._playlist.append(url)
            self._playlist_index = len(self._playlist) - 1
            self._player.setSource(url)
            self._player.play()

    @Slot()
    def playPauseClicked(self):
        if self._player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self._player.pause()
        elif self._player.playbackState() == QMediaPlayer.PlaybackState.PausedState:
            self._player.play()

    @Slot()
    def _ensure_stopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()

    @Slot()
    def previous_clicked(self):
        # Go to previous track if we are within the first 5 seconds of playback
        # Otherwise, seek to the beginning.
        if self._player.position() <= 5000 and self._playlist_index > 0:
            self._playlist_index -= 1
            self._playlist.previous()
            self._player.setSource(self._playlist[self._playlist_index])
        else:
            self._player.setPosition(0)

    @Slot()
    def next_clicked(self):
        if self._playlist_index < len(self._playlist) - 1:
            self._playlist_index += 1
            self._player.setSource(self._playlist[self._playlist_index])

    @Slot("QMediaPlayer::PlaybackState")
    def update_buttons(self, state):
        media_count = len(self._playlist)
        # self._play_action.setEnabled(media_count > 0 and state != QMediaPlayer.PlayingState)
        icon = QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause,
                               self.style().standardIcon(QStyle.SP_MediaPause))
        if state == QMediaPlayer.PlaybackState.PausedState:
            icon = QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart,
                                   self.style().standardIcon(QStyle.SP_MediaPlay))
        self._play_action.setIcon(icon)
        # self._pause_action.setEnabled(state == QMediaPlayer.PlayingState)
        self._stop_action.setEnabled(state != QMediaPlayer.StoppedState)
        self._previous_action.setEnabled(self._player.position() > 0)
        self._next_action.setEnabled(media_count > 1)

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)

    @Slot("QMediaPlayer::Error", str)
    def _player_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)

    @Slot()
    def setVolume(self):
        self.volumeValue = QAudio.convertVolume(self._volume_slider.value() / 100.0,
                                                QAudio.VolumeScale.LogarithmicVolumeScale,
                                                QAudio.VolumeScale.LinearVolumeScale)
        self._audio_output.setVolume(self.volumeValue)

    def openWindow(self):
        available_geometry = self.screen().availableGeometry()
        self.resize(available_geometry.width() / 3,
                    available_geometry.height() / 2)
        self.show()

    @property
    def get_position_changed_signal(self):
        return self._player.positionChanged

    def get_video_position(self):
        return self._player.position()

    def closeEvent(self, event):
        """Ensure widget is deleted when closed."""
        self._player.stop()
        self._player.deleteLater()
        self.deleteLater()  # Schedule deletion
        gc.collect()
        event.accept()  # Allow closing


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = VideoPlayerWindow()
    available_geometry = main_win.screen().availableGeometry()
    main_win.resize(available_geometry.width() / 3,
                    available_geometry.height() / 2)
    main_win.show()
    sys.exit(app.exec())
