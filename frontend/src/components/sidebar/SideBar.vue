<template>
  <v-navigation-drawer v-model="drawer" app>
    <v-list v-for="app of djangoapps" :key="app.name" dense>
      <DjangoApp :name="app.name" :icon="app.icon" :link="app.url"></DjangoApp>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mdiInboxMultiple, mdiHome } from "@mdi/js";
import DjangoApp from "@/components/sidebar/DjangoApp";
export default {
  name: "SideBar",
  components: { DjangoApp },
  data() {
    return {
      djangoapps: [
        { name: "Home", icon: mdiHome, url: "/" },
        { name: "Inventory", icon: mdiInboxMultiple, url: "/inventory" },
      ],
    };
  },
};
</script>
