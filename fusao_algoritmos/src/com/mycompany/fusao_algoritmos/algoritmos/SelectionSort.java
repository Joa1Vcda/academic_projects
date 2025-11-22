package com.mycompany.fusao_algoritmos.algoritmos;

public class SelectionSort
{
    public static void printResult(int[] data)
    {
        int[] copy = data.clone();
        selectionSort(copy);

        int i = 0;

        for(  ; i < copy.length; i++)
        {
            System.out.println(copy[i]);
        }
    System.out.println();
    }

    public static long measureTime(int[] data) {
        int[] copy = data.clone(); // Trabalha com cópia
        selectionSort(copy);
        long startTime = System.nanoTime();
        selectionSort(copy);
        long endTime = System.nanoTime();
        return endTime - startTime;
    }

    // Código do loiros
    private static void selectionSort(int[] data)
    {
        for (int i = 0; i < data.length; i++)
        {
            int minIndex = i;

            for (int j = i + 1; j < data.length; j++)
            {
                if (data[j] < data[minIndex])
                {
                    minIndex = j;
                }
            }

            int temp = data[i];
            data[i] = data[minIndex];
            data[minIndex] = temp;
        }
    }
}