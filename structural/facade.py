# Facade is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.


class VideoFile:
    def do_complicated_stuff(self):
        print("VideoFile do something complicate")


class OggCompressionCodec:
    def do_complicated_stuff(self):
        print("OggCompressionCodec do something complicate")


class MPEG4CompressionCodec:
    def do_complicated_stuff(self):
        print("MPEG4CompressionCodec do something complicate")


class CodecFactory:
    def do_complicated_stuff(self):
        print("CodecFactory do something complicate")


class VideoConverter:
    def convert(self):
        cls1 = VideoFile()
        cls1.do_complicated_stuff()

        cls2 = OggCompressionCodec()
        cls2.do_complicated_stuff()

        cls3 = MPEG4CompressionCodec()
        cls3.do_complicated_stuff()

        cls4 = CodecFactory()
        cls4.do_complicated_stuff()


def main():
    converter = VideoConverter()
    converter.convert()


main()
