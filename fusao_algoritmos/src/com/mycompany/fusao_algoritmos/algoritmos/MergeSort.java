package com.mycompany.fusao_algoritmos.algoritmos;

public class MergeSort {

    // Método público para iniciar o merge sort
    public static void sort(int[] data) {
        if (data == null || data.length <= 1) return;
        mergeSort(data, 0, data.length - 1);
    }

    // Método público para imprimir resultados
    public static void printResult(int[] data) {
        int[] copy = data.clone(); // Cria cópia para não modificar o original
        sort(copy);

        System.out.println("Array ordenado:");
        for (int i = 0; i < copy.length; i++) {
            System.out.print(copy[i] + " ");
        }
        System.out.println();
    }

    // Método recursivo do merge sort
    private static void mergeSort(int[] data, int left, int right) {
        if (left < right) {
            int middle = left + (right - left) / 2;

            // Ordena as duas metades
            mergeSort(data, left, middle);
            mergeSort(data, middle + 1, right);

            // Combina as metades ordenadas
            merge(data, left, middle, right);
        }
    }

    // Método para combinar duas subarrays ordenadas
    private static void merge(int[] data, int left, int middle, int right) {
        // Tamanhos das subarrays
        int n1 = middle - left + 1;
        int n2 = right - middle;

        // Arrays temporárias
        int[] leftArray = new int[n1];
        int[] rightArray = new int[n2];

        // Copia dados para arrays temporárias
        for (int i = 0; i < n1; i++) {
            leftArray[i] = data[left + i];
        }
        for (int j = 0; j < n2; j++) {
            rightArray[j] = data[middle + 1 + j];
        }

        // Combina as arrays temporárias
        int i = 0, j = 0, k = left;

        while (i < n1 && j < n2) {
            if (leftArray[i] <= rightArray[j]) {
                data[k] = leftArray[i];
                i++;
            } else {
                data[k] = rightArray[j];
                j++;
            }
            k++;
        }

        // Copia elementos restantes da leftArray
        while (i < n1) {
            data[k] = leftArray[i];
            i++;
            k++;
        }

        // Copia elementos restantes da rightArray
        while (j < n2) {
            data[k] = rightArray[j];
            j++;
            k++;
        }
    }

    // Método utilitário para medir tempo de execução
    public static long measureTime(int[] data) {
        int[] copy = data.clone();
        long startTime = System.nanoTime();
        sort(copy);
        long endTime = System.nanoTime();
        return endTime - startTime;
    }
}
