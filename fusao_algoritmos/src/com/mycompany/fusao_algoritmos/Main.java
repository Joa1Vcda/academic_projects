package com.mycompany.fusao_algoritmos;

import com.mycompany.fusao_algoritmos.algoritmos.*;
import com.mycompany.fusao_algoritmos.utils.DataSets;

public class Main {
    public static void main(String[] args) {
        System.out.println("=== ENCONTRANDO n0 ===");
        findN0();

        System.out.println("\n=== TESTANDO COM 10.000 ELEMENTOS ===");
        testWith10000();
    }

    private static void findN0() {
        int[] sizes = {10, 50, 100, 200, 500, 1000};

        for (int size : sizes) {
            int[] data = DataSets.generateOrderedArray(size);

            long timeMerge = MergeSort.measureTime(data);
            long timeSelection = SelectionSort.measureTime(data);

            System.out.printf("n=%4d | Merge: %8d ns | Selection: %8d ns",
                    size, timeMerge, timeSelection);

            if (timeMerge < timeSelection) {
                System.out.println(" ← Merge mais rápido!");
            } else {
                System.out.println(" ← Selection mais rápido!");
            }
        }
    }

    private static void testWith10000() {
        int[] ordered = DataSets.getOrdered10000();
        int[] reversed = DataSets.getReversed10000();

        System.out.println("Ordenado - Merge: " + MergeSort.measureTime(ordered) + " ns");
        System.out.println("Inverso  - Merge: " + MergeSort.measureTime(reversed) + " ns");
    }
}