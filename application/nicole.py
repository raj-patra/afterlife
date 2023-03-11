import aiml, os

class NicoleBot:
    def __init__(self):
        self.kernel = aiml.Kernel()
        self.kernel.verbose(0)
        self.kernel.setBotPredicate("name", "Nicole")

        # Load/Learn Brain file
        if os.path.isfile("assets/bot_brain.brn"):
            self.kernel.bootstrap(brainFile="assets/bot_brain.brn")
        else:
            self.kernel.bootstrap(learnFiles="startup.xml", commands="LOAD AIML B")
            self.kernel.saveBrain("assets/bot_brain.brn")

        self.kernel.setPredicate("name", "Stranger")