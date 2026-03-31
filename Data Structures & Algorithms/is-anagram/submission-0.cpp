class Solution {
public:
    bool isAnagram(string s, string t) {

        unordered_map<char,int> map1;
        unordered_map<char,int> map2;
        for(int i = 0; i<s.size();i++){
            map1[s[i]] +=1;
        }
        for(int j = 0; j<t.size(); j++){
            map2[t[j]] +=1;
        }
        return map1 == map2;
    } 
};
