package com.mycompany.fusao_algoritmos.utils;

//tive que mudar aqui pra achar o n0 com mais precisão.
public class DataSets {

    public static int[] RetrieveUnorderedDataset(int size) {
        int[] unorderedDataset = new int[size];
        for (int i = 0; i < size; i++) {
            unorderedDataset[i] = size - i;  // [size, size-1, ..., 1]
        }
        return unorderedDataset;
    }

    public static int[] RetrieveOrderedDataset(int size) {
        int[] orderedDataset = new int[size];
        for (int i = 0; i < size; i++) {
            orderedDataset[i] = i + 1;  // [1, 2, 3, ..., size]
        }
        return orderedDataset;
    }

    // Mantém versões antigas para compatibilidade
    public static int[] RetrieveUnorderedDatasetTeste() {
        return RetrieveUnorderedDataset(10000);
    }

    public static int[] RetrieveOrderedDatasetTeste() {
        return RetrieveOrderedDataset(10000);
    }
}
