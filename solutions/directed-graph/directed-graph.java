/*
 Author: vedipen
*/

import java.io.*;
import java.util.*;

public class DirectedGraphCycle {
    /*
     Given Graph graph we can determine cycle in directed graph by using recursion stack
     which gives the number of elements processed in current recursion. If any element
     which is in current recursion comes again then we can surely say that there is a cycle.
     */

    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    // Checks whether the current node is visited
    static boolean vis[];
    // Keeps track whether the given element is in recursion stack or not
    static boolean recStack[];
    // No of vertices and edges in directed Graph
    static int vertices, numEdges;

    public static void main(String args[]) throws IOException {
        Scanner in = new Scanner(System.in);
        PrintWriter w = new PrintWriter(System.out);
        int testcases = in.nextInt();
        while(testcases-->0) {
            graph.clear();
            vertices = in.nextInt()+1;
            for (int i = 0; i < vertices; i++) {
                graph.add(new ArrayList<>());
            }
    
            numEdges = in.nextInt();
            for (int i = 0; i < numEdges; i++) {
                int x = in.nextInt();
                int y = in.nextInt();
                graph.get(x).add(y);
            }
            cycleDetectUtil();
        }
        w.close();
    }

    static void cycleDetectUtil() {
        vis = new boolean[vertices];
        recStack = new boolean[26];
        for (int i = 0; i < vertices; i++) {
            if (!vis[i]) {
                if (cycleDetect(i)) {
                    System.out.println("1");  //Cycle Detected
                    return;
                }
            };
        }
        System.out.println("0");  //No Cycle Found
    }

    static boolean cycleDetect(int i) {
        if (!vis[i]) {
            vis[i] = true;
            recStack[i] = true;
            for (int x : graph.get(i)) {
                if (!vis[x]) {
                    if (cycleDetect(x)) {
                        return true;
                    }
                } else if (recStack[x]) {
                    return true;
                }
            }
        }
        recStack[i] = false;
        return false;
    }
}
