import java.util.*;

public class BaseballScore {
	public int getScore(String[] scores) {
		Stack<Integer> stack = new Stack<Integer>();
		String[] special = {"Z", "X", "+"};
		int res = 0;
		for (String c: scores) {
			if (Arrays.asList(special).indexOf(c) == -1) {
				int score = Integer.parseInt(c);
				res += score;
				stack.push(score);
			}
			else if (c == "Z") {
				res -= stack.pop();
			}
			else if (c == "X") {
				int last = stack.pop();
				res += 2 * last;
				stack.push(2 * last);
			}
			else {
				int l1 = stack.pop();
				int l2 = stack.pop();
				res += l1 + l2;
				stack.push(l2);
				stack.push(l1);
				stack.push(l1+l2);
			}
			System.out.println(res);
		}
		return res;
	}

	public static void main(String[] args) {
        String[] scores = {"5", "-2", "4", "Z", "X", "9", "+", "+"};
        BaseballScore bs = new BaseballScore();
        int res = bs.getScore(scores);
        System.out.println(res);

        // String s1 = "([)]";
        // ValidParentheses vp1 = new ValidParentheses();
        // System.out.println(vp1.isValid(s1));
    }
}