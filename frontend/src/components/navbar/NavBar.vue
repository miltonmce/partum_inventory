<template>
  <div>
    <SideBar :drawer="drawer"></SideBar>
    <v-app-bar app color="indigo" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>{{ this.$route.meta.title }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn icon>
          <v-icon>{{ inboxIcon }}</v-icon>
        </v-btn>
        <UserOptions v-on="on"></UserOptions>
      </v-toolbar-items>
    </v-app-bar>
  </div>
</template>

<script>
import SideBar from "@/components/sidebar/SideBar";
import UserOptions from "@/components/navbar/UserOptions";
import { mdiEmail } from "@mdi/js";

export default {
  name: "Navbar",
  components: {
    SideBar,
    UserOptions,
  },
  data: () => ({
    drawer: false,
    inboxIcon: mdiEmail,
  }),
  methods: {},
};
</script>
