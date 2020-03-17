class Quest:

    def __init__(self, name, startDay, duration, value):
        self.name = name
        self.startDay = startDay
        self.duration = duration
        self.value = value


def createQuestsByDay(availableQuests):
    quests = {}
    for i in range(1,32):
        quests[i] = []

    for quest in availableQuests:
        quests[quest.startDay].append(quest)

    return quests


def chooseBestQuests_recursive(questsByDay, bestChoiceByDay, currentDay):
    if currentDay > 31:
        return [[], 0]

    if currentDay in bestChoiceByDay.keys():
        return bestChoiceByDay[currentDay]

    questsStartingToday = questsByDay[currentDay]

    bestQuests = []
    bestValueForToday = 0
    for quest in questsStartingToday:
        otherQuests, valueOfOthers = chooseBestQuests_recursive(questsByDay, bestChoiceByDay, currentDay + quest.duration)
        value = quest.value + valueOfOthers

        if value > bestValueForToday:
            bestQuests = [quest.name] + otherQuests
            bestValueForToday = value

    tomorrowQuests, tomorrowValue = chooseBestQuests_recursive(questsByDay, bestChoiceByDay, currentDay + 1)

    if tomorrowValue > bestValueForToday:
        bestChoiceByDay[currentDay] = [tomorrowQuests, tomorrowValue]
        return [tomorrowQuests, tomorrowValue]
    else:
        bestChoiceByDay[currentDay] = [bestQuests, bestValueForToday]
        return [bestQuests, bestValueForToday]


def chooseBestQuests(availableQuests):
    questsByDay = createQuestsByDay(availableQuests)
    return chooseBestQuests_recursive(questsByDay, {}, 1)
