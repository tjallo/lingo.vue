<template>
  <v-app>
    <v-container class="grey lighten-5">
      <v-row no-gutters v-for="word in guesses" :key="word">
        <v-col
          v-for="letter in word"
          :key="letter"
          class="pa-2"
          :class="letter[1]"
          outlined
          tile
          align="center"
        >
          {{ letter[1] }}
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import { fiveCharWords, sixCharWords, sevenCharWords } from "./scripts/words";

export default {
  name: "App",

  components: {},

  data: () => ({
    fiveCharWords: fiveCharWords,
    sixCharWords: sixCharWords,
    sevenCharWords: sevenCharWords,
    word: "",
    methods: {
      getWord: function () {
        self.word = "words";
      },
    },
    guesses: [
      [
        ["l", "red"],
        ["e", "green"],
        ["t", "red"],
        ["t", "green"],
        ["e", "red"],
        ["r", "red"],
      ],
      [
        ["l", "red"],
        ["e", "green"],
        ["t", "red"],
        ["t", "green"],
        ["e", "red"],
        ["r", "red"],
      ],
      [
        ["l", "red"],
        ["e", "green"],
        ["t", "red"],
        ["t", "green"],
        ["e", "red"],
        ["r", "red"],
      ],
      [
        ["l", "red"],
        ["e", "green"],
        ["t", "red"],
        ["t", "green"],
        ["e", "red"],
        ["r", "red"],
      ],
      [
        ["l", "red"],
        ["e", "green"],
        ["t", "red"],
        ["t", "green"],
        ["e", "red"],
        ["r", "red"],
      ],
    ],
  }),
};
</script>
