<template>
  <v-card :to="link" color="#428bca">
    <v-row>
      <v-col class="text-center" cols="12">
        <v-icon size="100">{{icon}}</v-icon>
        <v-card-title class="justify-center">{{title}}</v-card-title>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  name: "HelloWorld",
  props: ["title", "icon", "link"],
};
</script>