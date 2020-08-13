<template>
  <div>
    <SideBar :drawer="drawer"></SideBar>
    <v-app-bar app color="indigo" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>{{ this.$route.meta.title }}</v-toolbar-title>
    </v-app-bar>
  </div>
</template>

<script>
import SideBar from "@/components/sidebar/SideBar";

export default {
  name: "Navbar",
  components: {
    SideBar,
  },
  data: () => ({
    drawer: false,
  }),
  methods: {},
};
</script>
