<template>
  <v-app id="inspire">
    <NavBar></NavBar>
    <v-main>
      <router-view></router-view>
    </v-main>
    <v-footer color="indigo" app>
      <span class="white--text">&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
import NavBar from "./components/navbar/NavBar";
export default {
  props: {
    source: String,
  },
  components: {
    NavBar,
  },
  data: () => ({
    drawer: null,
  }),
};
</script>
