package com.mycompany.fusao_algoritmos.algoritmos;

public class SelectionSort
{
    public static void PrintResult(int data[])
    {
        SelectionSort(data);

        int i = 0;

        for(  ; i < data.length; i++)
        {
            System.out.println(data[i]);
        }
    }

    private static void SelectionSort(int data[])
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