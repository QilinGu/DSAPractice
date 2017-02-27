import java.util.*;

public class ValidParentheses{
	public boolean isValid(String s) {
		Stack<Character> stack = new Stack<Character>();
		for (Character c: s.toCharArray()) {
			if (c == '{') stack.push('}');
			else if (c == '[') stack.push(']');
			else if (c == '(') stack.push(')');
			else if (stack.isEmpty() || c != stack.pop())
				return false;
		}
		return stack.isEmpty();
	}

	public static void main(String[] args) {
        String s = "()[]{}";
        ValidParentheses vp = new ValidParentheses();
        System.out.println(vp.isValid(s));

        String s1 = "([)]";
        ValidParentheses vp1 = new ValidParentheses();
        System.out.println(vp1.isValid(s1));
    }
}