from game.bot_strategy import NoviceBot, DefenseBot, AttackBot, GuruBot, AIBot

class BotFactory:
    @staticmethod
    def get_bot(difficulty):
        if difficulty == "Novice":
            return NoviceBot()
        elif difficulty == "Defense":
            return DefenseBot()
        elif difficulty == "Attack":
            return AttackBot()
        elif difficulty == "Guru":
            return GuruBot()
        elif difficulty == "AI":
            return AIBot()
        else:
            return NoviceBot()
