package com.mycompany.fusao_algoritmos.utils;

import java.util.stream.IntStream;

public class DataSets
{
    public static int[] RetrieveUnorderedDataset()
    {
        int[] unorderedDataset = IntStream.iterate(10000, i -> i >= 1, i -> i - 1).toArray();
        return unorderedDataset;
    }

    public static int[] RetrieveOrderedDataset()
    {
        int[] orderedDataset = IntStream.rangeClosed(1, 10000).toArray();
        return orderedDataset;
}
}