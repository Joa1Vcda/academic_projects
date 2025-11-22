package com.mycompany.fusao_algoritmos.algoritmos;

import java.util.Arrays;

public class HybridSort {
    private final int n0;

    public HybridSort(int n0) {
        this.n0 = n0;
    }

    // Método público para medir tempo
    public static long measureTime(int[] data, int n0) {
        int[] copy = data.clone();
        HybridSort sorter = new HybridSort(n0);
        long startTime = System.nanoTime();
        sorter.hybridSort(copy);
        long endTime = System.nanoTime();
        return endTime - startTime;
    }

    public static void printResult(int[] data, int n0) {
        int[] copy = data.clone();
        new HybridSort(n0).hybridSort(copy);

        for (int i = 0; i < copy.length; i++) {
            System.out.print(copy[i] + " ");
        }
        System.out.println();
    }

    // A ideia é a seguinte, se ele for menor que n0, ele só usa o selection, porém para casos de >n0 ele precisa se
    // dividir até alcançar o n0, ou seja, cria-se vários vetores com uma quantidade de elementos menor que o n0
    // e então nesse estado o Selection ordena esses micro-vetores, porém esses micro-vetores não estão ordenados entre
    // si, apenas dentro de si, e aí que o merge-sort entra, ele ordena os micro-vetores que já estão ordenados
    // na minha cabeça ele parece ser mais lento para todos os casos
    private void hybridSort(int[] data) {
        int length = data.length;

        // Se for pequeno, usa SelectionSort
        if (length <= n0) {
            selectionSort(data);
            return;
        }

        // Divisão do vetores menores que eu citei ocorre aqui
        int mid = data.length / 2;
        int[] left = Arrays.copyOfRange(data, 0, mid);
        int[] right = Arrays.copyOfRange(data, mid, data.length);

        // Vai dividindo em mini vetores e ordenando quando os vetores tiverem o tamanho = n0
        hybridSort(left);
        hybridSort(right);

        //reorganiza os vetores :)
        merge(left, right, data);
    }

    // CÓPIA IDÊNTICA do Little blond code
    private static void selectionSort(int[] data) {
        for (int i = 0; i < data.length; i++) {
            int minIndex = i;
            for (int j = i + 1; j < data.length; j++) {
                if (data[j] < data[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = data[i];
            data[i] = data[minIndex];
            data[minIndex] = temp;
        }
    }

    // expliquei o porque da alteração lá no MergeSort.java
    private static void merge(int[] left, int[] right, int[] data) {
        int leftSize = left.length;
        int rightSize = right.length;
        // Versão do little blond abaixo
        //int leftSize = data.length / 2;
        //int rightSize = data.length - leftSize;
        int i = 0, l = 0, r = 0;

        while (l < leftSize && r < rightSize) {
            if (left[l] < right[r]) {
                data[i] = left[l];
                i++;
                l++;
            } else {
                data[i] = right[r];
                i++;
                r++;
            }
        }

        while (l < leftSize) {
            data[i] = left[l];
            i++;
            l++;
        }

        while (r < rightSize) {
            data[i] = right[r];
            i++;
            r++;
        }
    }
}