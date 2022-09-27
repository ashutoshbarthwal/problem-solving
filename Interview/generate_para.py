# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

stored_para = dict()
stored_para[0] = [""]
stored_para[1] = ["()"]
def generate_para(n,stored_para={0:[""],1:["()"]}):
    
    result = []
    if n in stored_para:
        return stored_para[n]
    for i in range(n):
        for j in generate_para(i,stored_para):
            for k in generate_para(n-i-1,stored_para):
                result.append("(" + j + ")" + k)
    stored_para[n] = result
    return result

print(len(generate_para(6)))

import cProfile
cProfile.run("generate_para(4,stored_para)")
    

