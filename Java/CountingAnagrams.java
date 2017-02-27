import java.util.*;

public class CountingAnagrams {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> list = new ArrayList<>();
        if (s == null || s.length() == 0 || p == null || p.length() == 0) return list;
        int[] hash = new int[256]; //character hash

        for (char c : p.toCharArray()) {
            hash[c]++;
        }
        int left = 0, right = 0, count = p.length();

        while (right < s.length()) {
            if (hash[s.charAt(right)] >= 1) {
                count--;
            }
            hash[s.charAt(right)]--;
            right++;

            if (count == 0) {
                list.add(left);
            }
            if (right - left == p.length() ) {
                if (hash[s.charAt(left)] >= 0) {
                    count++;
                }
                hash[s.charAt(left)]++;
                left++;
            }
        }
        return list;
    }

    public static void main(String[] args) {
        String s = "cbaebabacd";
        String p = "abc";
        CountingAnagrams ca = new CountingAnagrams();
        List<Integer> list = ca.findAnagrams(s, p);
        StringBuilder sb = new StringBuilder();
        for (Integer i : list)
        {
            sb.append(i);
            sb.append(" ");
        }
        System.out.println(sb.toString());

        String s1 = "abab";
        String p1 = "ab";
        List<Integer> list1 = ca.findAnagrams(s1, p1);
        StringBuilder sb1 = new StringBuilder();
        for (Integer i : list1)
        {
            sb1.append(i);
            sb1.append(" ");
        }
        System.out.println(sb1.toString());
    }
}