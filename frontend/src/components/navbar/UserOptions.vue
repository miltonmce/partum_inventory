<template>
  <v-menu open-on-hover bottom offset-y>
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="#428bca" dark v-bind="attrs" v-on="on">
        Login
      </v-btn>
    </template>

    <v-list>
      <v-list-item v-for="(item, index) in items" :key="index">
        <v-list-item-title>{{ item.title }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  name: "UserOptions",
};
</script>
