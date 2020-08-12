<template>
  <v-list-item :to="link">
    <v-list-item-action>
      <v-icon>{{ icon }}</v-icon>
    </v-list-item-action>
    <v-list-item-content>
      <v-list-item-title>{{ name }}</v-list-item-title>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
export default {
  name: "DjangoApp",
  components: {},
  props: ["link", "name", "icon"],
};
</script>
