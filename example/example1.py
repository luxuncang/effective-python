from effective import Effective

effective1 = Effective(a=lambda x: f"effective1: {x}")


def main():

    effective2 = Effective(b=lambda *x: f"effective2: {x}")

    def main1():

        effective3 = Effective(c=lambda *x, **y: f"effective3: {x} {y}")

        def main2():

            effective4 = Effective(d=lambda x: f"effective4: {x}")
            effective5 = Effective(fields={'d': lambda x: f"effective5: {x}"})

            a, b, c, d = (
                Effective.perform("a", 1),
                Effective.perform("b", 1, 2),
                Effective.perform("c", 1, 2, 3, c=(1, 2, 3)),
                Effective.perform("d", 4),
            )
            print(a, b, c, d, sep="\n")

        return main2()

    return main1()


main()