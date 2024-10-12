from typing import List
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        table: dict[str, int] = defaultdict(int)
        for entry in cpdomains:
            content: List[str] = entry.split(' ')
            count: int = int(content[0])
            domains: List[str] = content[1].split('.')
            prefixes: List[str] = [domains[-1]]
            current_prefix: str = domains[-1]
            for i in range(len(domains) - 2, -1, -1):
                prefixes.append(f'{domains[i]}.{current_prefix}')
                current_prefix = f'{domains[i]}.{current_prefix}'
            for prefix in prefixes:
                table[prefix] += count
        visits: List[str] = []
        for entry in table:
            result: str = f'{table[entry]} {entry}'
            visits.append(result)
        return visits