survey_results = [
    ["Python", "JavaScript", "C++"],         
    ["Python", "JavaScript", "C#"],           
    ["Python", "Java"],                       
    ["Python", "C++", "JavaScript"],          
    ["Python", "JavaScript", "C++", "Java"],   
]
sets_list = [set(choices) for choices in survey_results]

ans1 = set.intersection(*sets_list)
print(f"1. Languages chosen by all participants: {ans1}")

counts = {}
for s in sets_list:
    for lang in s:
        counts[lang] = counts.get(lang, 0) + 1

ans2 = {lang for lang, count in counts.items() if count == 1}
print(f"2. Languages only chosen by one participant: {ans2}")

ans3 = len(counts)
print(f"3. Number of unique languages: {ans3}")

ans4 = {lang for lang, count in counts.items() if count == 2}
print(f"4. Languages chosen by exactly two participants: {ans4}")

ans5 = []
n = len(sets_list)
for i in range(n):
    for j in range(i + 1, n):
        if sets_list[i] == sets_list[j]:
            ans5.append([i + 1, j + 1])
print(f"5. Participants with the same set of languages: {ans5}")