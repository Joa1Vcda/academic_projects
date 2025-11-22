package com.mycompany.fusao_algoritmos.algoritmos;

public class MergeSort {

    // Loirin Issues
    public static void PrintResult(int[] data)
    {
        int[] copy = data.clone();
        mergeSort(copy);
        for (int i = 0; i < copy.length; i++)
        {
            System.out.println(copy[i] + " ");
        }
    System.out.println();
    }

    public static long measureTime(int[] data) {
        int[] copy = data.clone();
        mergeSort(copy);
        long startTime = System.nanoTime();
        mergeSort(copy);
        long endTime = System.nanoTime();
        return endTime - startTime;
    }
    // Loirin mecanics
    private static void mergeSort(int[] data)
    {
        int length = data.length;

        // Caso base
        if (length <= 1) return;

        int middle = length / 2;

        int[] left = new int[middle];
        int[] right = new int[length - middle];

        int i = 0;
        int j = 0;

        for (; i < length; i++)
        {
            if (i < middle)
                left[i] = data[i];

            else
            {
                right[j] = data[i];
                j++;
            }
        }

        mergeSort(left);
        mergeSort(right);
        merge(left, right, data);
    }

    // Código do loirin só mudando a declaração do left size e do right size, o dele funcionava mas só para vetores
    //de índice par, como vou usar essa base pra calcular o n0, é importante a divisão ser feita da forma que eu fiz
    private static void merge(int[] left, int[] right, int[] data)
    {
        int leftSize = left.length;
        int rightSize = right.length;
        int i = 0, l = 0, r = 0;

        while (l < leftSize && r < rightSize)
        {
            if (left[l] < right[r])
            {
                data[i] = left[l];
                i++;
                l++;
            }
            else
            {
                data[i] = right[r];
                i++;
                r++;
            }
        }

        while (l < leftSize)
        {
            data[i] = left[l];
            i++;
            l++;
        }

        while (r < rightSize)
        {
            data[i] = right[r];
            i++;
            r++;
        }
    }
}

