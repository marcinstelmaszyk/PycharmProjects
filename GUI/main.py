from brpf.processor import BRPF


class Test:
    @staticmethod
    def print(s):
        print(id(s))
        s.append("gone")


if __name__ == "__main__":
    # processor = BRPF()
    # processor.configure()
    # processor.run()
    # processor.cleanup()
    a = ["Hello world"]
    print(id(a))
    Test.print(a)
    print(a)

