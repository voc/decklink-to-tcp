import argparse

__all__ = ['Args']

Args = None


def parse():
    global Args

    parser = argparse.ArgumentParser(description='Voctocore')
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help="Also print INFO and DEBUG messages.")

    parser.add_argument('-C', '--color',
                        action='store',
                        choices=['auto', 'always', 'never'],
                        default='auto',
                        help="Control the use of colors in the Log-Output")

    parser.add_argument('-t', '--timestamp', action='store_true',
                        help="Enable timestamps in the Log-Output")

    parser.add_argument('-m', '--mode', action='store', required=True,
                        help="Decklink-Mode, see `gst-inspect-1.0 decklinkvideosrc` for possible values")

    parser.add_argument('-c', '--connection', action='store', required=True,
                        help="Decklink Video-Connection-Type, see `gst-inspect-1.0 decklinkvideosrc` for possible values")

    parser.add_argument('-d', '--device-number', action='store', type=int, dest='device', required=True,
                        help="Decklink Device-Number, 0-based")

    parser.add_argument('-a', '--audio-channels', action='store', type=int, default=2, dest='channels',
                        help="Number of Audio-Channels: 2, 8 or 16. >2 requires GStreamer >= 1.12.3")

    parser.add_argument('-A', '--audio-connection', action='store', default='auto', dest='audioconnection',
                        help="Decklink Audio-Connection-Type, see `gst-inspect-1.0 decklinkvideosrc` for possible values")

    Args = parser.parse_args()
