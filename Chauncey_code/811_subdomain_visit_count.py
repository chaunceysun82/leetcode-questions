class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # Time: O(n)
        # Space: O(n)

        dict = {}
        for string in cpdomains: 
            count, cpdomain = string.split(' ', 1)
            domain_list = self.get_domains_list(cpdomain)

            for domain in domain_list:
                if domain in dict:
                    dict[domain] = dict.get(domain) + int(count)
                else:
                    dict[domain] = int(count)

        output = []
        for key, value in dict.items():
            output.append(str(value) + ' ' + key)

        return output


    def get_domains_list(self, string) -> List[str]:  # Time: O(N)
        splited_sections = string.split('.')
        domains_list = []

        for i in range(len(splited_sections)):
            domains_list.append('.'.join(splited_sections[i::]))
        return domains_list