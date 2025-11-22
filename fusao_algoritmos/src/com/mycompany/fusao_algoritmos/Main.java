package com.mycompany.fusao_algoritmos;

import com.mycompany.fusao_algoritmos.algoritmos.*;
import com.mycompany.fusao_algoritmos.utils.DataSets;
import java.util.Arrays;

public class Main {
    private static final int REPETITIONS = 100;
    private static final int DATA_SIZE = 10000;

    static void main(String[] args) {
        System.out.println("\n" + "=== TRABALHO DE ANÁLISE DE ALGORITMOS ===");
        System.out.println("Algoritmos: Selection Sort (Quadrático) vs Merge Sort (Log-linear)");
        System.out.println("Experimentos: " + REPETITIONS + " repetições\n");

        // 1. Encontrar n0 empiricamente
        int n0ordenado = encontrarN0ordenado();
        int n0invertido = encontrarN0invertido();
        System.out.println("\n" + "=".repeat(50));
        System.out.println("n0 para o vetor ordenado encontrado: " + n0ordenado);
        System.out.println("n0 para o vetor invertido encontrado: " + n0invertido);
        System.out.println("=".repeat(50) + "\n");

        // 2. Executar experimentos principais
        executarExperimentosCompletos(n0ordenado, n0invertido);
    }

    // Método para encontrar n0 empiricamente
    private static int encontrarN0ordenado() {
        System.out.println("=== FASE 1: ENCONTRANDO n0 para o vetor ordenado ===");

        int[] tamanhosTeste = {10, 25, 35, 42, 50, 55, 60, 75, 100, 200, 500, 1000};
        int melhorN0ordenado = 50; // valor padrão

        System.out.printf("%-10s | %-15s | %-15s | %-10s%n",
                "Tamanho", "Selection Sort", "Merge Sort", "Mais Rápido");
        System.out.println("-".repeat(60));

        for (int tamanho : tamanhosTeste) {
            int[] dadosOrdenados = DataSets.RetrieveOrderedDataset(tamanho);

            long tempoSelection = 0, tempoMerge = 0;
            int amostras = 1000;

            for (int i = 0; i < amostras; i++) {
                tempoSelection += SelectionSort.measureTime(Arrays.copyOf(dadosOrdenados, tamanho));
                tempoMerge += MergeSort.measureTime(Arrays.copyOf(dadosOrdenados, tamanho));
            }

            tempoSelection /= amostras;
            tempoMerge /= amostras;

            String maisRapido = tempoMerge < tempoSelection ? "MERGE" : "SELECTION";
            System.out.printf("%-10d | %-15d | %-15d | %-10s%n",
                    tamanho, tempoSelection, tempoMerge, maisRapido);

            // Atualiza n0 quando Merge Sort se tornar consistentemente mais rápido
            if (tempoMerge < tempoSelection) {
                melhorN0ordenado = tamanho;
                // quando corrigir a anomalia que eu defini no grupo, tira a linha abaixo de comentário que ele vai
                // parar no n0
                //break;
            }
        }

        return melhorN0ordenado;
    }

    private static int encontrarN0invertido() {
        System.out.println(" ");

        int[] tamanhosTeste = {10, 25, 35, 42, 50, 55, 60, 75, 100, 200, 500, 1000};
        int melhorN0invertido = 50; // valor padrão

        System.out.printf("%-10s | %-15s | %-15s | %-10s%n",
                "Tamanho", "Selection Sort", "Merge Sort", "Mais Rápido");
        System.out.println("-".repeat(60));

        for (int tamanho : tamanhosTeste) {
            int[] dadosInvertido = DataSets.RetrieveUnorderedDataset(tamanho);

            long tempoSelection = 0, tempoMerge = 0;
            int amostras = 100;

            for(int i = 0; i < amostras; i++) {
                tempoSelection += SelectionSort.measureTime(Arrays.copyOf(dadosInvertido, tamanho));
                tempoMerge += MergeSort.measureTime(Arrays.copyOf(dadosInvertido, tamanho));
            }

            tempoSelection /= amostras;
            tempoMerge /= amostras;

            String maisRapido = tempoMerge < tempoSelection ? "MERGE" : "SELECTION";
            System.out.printf("%-10d | %-15d | %-15d | %-10s%n",
                    tamanho, tempoSelection, tempoMerge, maisRapido);

            // Atualiza n0 quando Merge Sort se tornar consistentemente mais rápido
            if (tempoMerge < tempoSelection) {
                melhorN0invertido = tamanho;
                // quando corrigir a anomalia que eu defini no grupo, tira a linha abaixo de comentário que ele vai
                // parar no n0
                //break;
            }
        }
        return melhorN0invertido;
    }

    private static void executarExperimentosCompletos(int n0ordenado,int n0invertido) {
        System.out.println("=== FASE 2: EXECUTANDO EXPERIMENTOS ===");

        // Carregar datasets
        int[] dadosOrdenados = DataSets.RetrieveOrderedDatasetTeste();
        int[] dadosInvertidos = DataSets.RetrieveUnorderedDatasetTeste();

        System.out.println("Tamanho dos datasets: " + DATA_SIZE + " elementos");
        System.out.println("n0 utilizado para o vetor ordenado: " + n0ordenado);
        System.out.println("n0 utilizado para o vetor invertido: " + n0invertido);
        System.out.println("Repetições: " + REPETITIONS);

        // Executar para dados ordenados
        System.out.println("\n" + "═".repeat(70));
        System.out.println("RESULTADOS - DADOS ORDENADOS");
        System.out.println("═".repeat(70));

        ResultadoExperimento resultadosOrdenadosSelection = executarAlgoritmo(
                "Selection Sort", dadosOrdenados, REPETITIONS, false, 0);
        ResultadoExperimento resultadosOrdenadosMerge = executarAlgoritmo(
                "Merge Sort", dadosOrdenados, REPETITIONS, false, 0);
        ResultadoExperimento resultadosOrdenadosHybrid = executarAlgoritmo(
                "Hybrid Sort", dadosOrdenados, REPETITIONS, true, n0ordenado);

        exibirResultados(resultadosOrdenadosSelection);
        exibirResultados(resultadosOrdenadosMerge);
        exibirResultados(resultadosOrdenadosHybrid);

        // Executar para dados invertidos
        System.out.println("\n" + "═".repeat(70));
        System.out.println("RESULTADOS - DADOS INVERTIDOS");
        System.out.println("═".repeat(70));

        ResultadoExperimento resultadosInvertidosSelection = executarAlgoritmo(
                "Selection Sort", dadosInvertidos, REPETITIONS, false, 0);
        ResultadoExperimento resultadosInvertidosMerge = executarAlgoritmo(
                "Merge Sort", dadosInvertidos, REPETITIONS, false, 0);
        ResultadoExperimento resultadosInvertidosHybrid = executarAlgoritmo(
                "Hybrid Sort", dadosInvertidos, REPETITIONS, true, n0invertido);

        exibirResultados(resultadosInvertidosSelection);
        exibirResultados(resultadosInvertidosMerge);
        exibirResultados(resultadosInvertidosHybrid);
    }

    // Método para executar um algoritmo múltiplas vezes
    private static ResultadoExperimento executarAlgoritmo(String nomeAlgoritmo, int[] dados, int repeticoes,
                                                          boolean ehHibrido, int n0) {
        long[] tempos = new long[repeticoes];

        for (int i = 0; i < repeticoes; i++) {
            int[] copiaDados = Arrays.copyOf(dados, dados.length);
            long inicio = System.nanoTime();

            if (ehHibrido) {
                HybridSort.measureTime(copiaDados, n0);
            } else {
                switch (nomeAlgoritmo) {
                    case "Selection Sort":
                        SelectionSort.measureTime(copiaDados);
                        break;
                    case "Merge Sort":
                        MergeSort.measureTime(copiaDados);
                        break;
                }
            }

            long fim = System.nanoTime();
            tempos[i] = fim - inicio;
        }

        return new ResultadoExperimento(nomeAlgoritmo, tempos);
    }

    // Método para exibir resultados formatados
    private static void exibirResultados(ResultadoExperimento resultado) {
        System.out.printf("\n%s:%n", resultado.nomeAlgoritmo);
        System.out.printf("  Mínimo:     %,12d ns%n", resultado.minimo);
        System.out.printf("  Máximo:     %,12d ns%n", resultado.maximo);
        System.out.printf("  Médio:      %,12.2f ns%n", resultado.media);
        System.out.printf("  Moda:       %,12d ns%n", resultado.moda);
        System.out.printf("  Desvio Pad: %,12.2f ns%n", resultado.desvioPadrao);
    }
    // Classe para armazenar resultados do experimento
    static class ResultadoExperimento {
        String nomeAlgoritmo;
        long minimo;
        long maximo;
        double media;
        long moda;
        double desvioPadrao;

        ResultadoExperimento(String nomeAlgoritmo, long[] tempos) {
            this.nomeAlgoritmo = nomeAlgoritmo;
            calcularEstatisticas(tempos);
        }

        private void calcularEstatisticas(long[] tempos) {
            // Valores básicos
            this.minimo = Arrays.stream(tempos).min().getAsLong();
            this.maximo = Arrays.stream(tempos).max().getAsLong();
            this.media = Arrays.stream(tempos).average().getAsDouble();

            // Moda (valor mais frequente)
            this.moda = calcularModa(tempos);

            // Desvio padrão
            double variancia = 0;
            for (long tempo : tempos) {
                variancia += Math.pow(tempo - media, 2);
            }
            this.desvioPadrao = Math.sqrt(variancia / tempos.length);
        }

        private long calcularModa(long[] tempos) {
            // Arredonda para microssegundos para evitar moda muito específica
            long[] arredondados = Arrays.stream(tempos)
                    .map(t -> t / 1000) // converte para microssegundos
                    .toArray();

            // Conta frequências
            java.util.Map<Long, Integer> frequencias = new java.util.HashMap<>();
            for (long tempo : arredondados) {
                frequencias.put(tempo, frequencias.getOrDefault(tempo, 0) + 1);
            }

            // Encontra a moda
            long moda = arredondados[0];
            int maxFrequencia = 0;
            for (java.util.Map.Entry<Long, Integer> entry : frequencias.entrySet()) {
                if (entry.getValue() > maxFrequencia) {
                    maxFrequencia = entry.getValue();
                    moda = entry.getKey();
                }
            }

            return moda * 1000; // converte de volta para nanossegundos
        }
    }
}