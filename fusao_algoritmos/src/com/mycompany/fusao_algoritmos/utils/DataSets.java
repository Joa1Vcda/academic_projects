package com.mycompany.fusao_algoritmos.utils;

import java.util.Random;
import java.util.stream.IntStream;

public class DataSets {
    private static final Random random = new Random();

    // Gera array ORDENADO de tamanho específico
    public static int[] generateOrderedArray(int size) {
        return IntStream.rangeClosed(1, size).toArray();
    }

    // Gera array em ORDEM INVERSA de tamanho específico
    public static int[] generateReversedArray(int size) {
        return IntStream.iterate(size, i -> i - 1)
                .limit(size)
                .toArray();
    }

    // Métodos específicos para 10.000 elementos (conforme seu trabalho)
    public static int[] getOrdered10000() {
        return generateOrderedArray(10000);
    }

    public static int[] getReversed10000() {
        return generateReversedArray(10000);
    }

}