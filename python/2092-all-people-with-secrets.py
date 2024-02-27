from typing import *

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        def process(queue: List[List[int]], secret_table: dict, knows_secret: dict):
            table = dict()
            for entry in queue:
                if entry[0] not in table:
                    table[entry[0]] = [entry[1]]
                else:
                    table[entry[0]].append(entry[1])

                if entry[1] not in table:
                    table[entry[1]] = [entry[0]]
                else:
                    table[entry[1]].append(entry[0])

            for entry in table:
                if entry in secret_table:
                    visited = dict()
                    dfs(entry, n, visited, table, knows_secret)

        def dfs(person: int, n: int, visited: dict, table: dict, knows_secret: dict):
            visited[person] = True
            knows_secret[person] = True
            if person in table:
                for neighbor in table[person]:
                    if neighbor not in visited:
                        dfs(neighbor, n, visited, table, knows_secret)

        meetings.sort(key=lambda item: item[2])

        meeting_groups = {}
        for meeting in meetings:
            time = meeting[2]
            if time not in meeting_groups:
                meeting_groups[time] = [meeting]
            else:
                meeting_groups[time].append(meeting)

        knows_secret = {0: True, firstPerson: True}
        
        for group in meeting_groups.values():
            queue = group
            process(queue, knows_secret, knows_secret)

        return [person for person, knows in knows_secret.items() if knows]