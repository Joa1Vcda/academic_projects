package com.mycompany.fusao_algoritmos.algoritmos;

public class MergeSort {

    // Método público para imprimir resultados
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

    // Método recursivo do merge sort
    private static void mergeSort(int[] data)
    {
        int length = data.length;

        // Caso base
        if (length <= 1) return;

        int middle = length / 2;

        int[] left = new int[middle];
        int[] right = new int[length - middle];

        int i = 0; // Para a array esquerda
        int j = 0; // Para a array direita

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

    // Método para combinar duas subarrays ordenadas
    private static void merge(int[] left, int[] right, int[] data)
    {
        int leftSize = data.length / 2;
        int rightSize = data.length - leftSize;
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

    // Método utilitário para medir tempo de execução
    public static long measureTime(int[] data) {
        int[] copy = data.clone();
        long startTime = System.nanoTime();
        mergeSort(copy);
        long endTime = System.nanoTime();
        return endTime - startTime;
    }
}

