<template>
  <v-container>
    <v-row>
      <v-col v-for="item of items" :key="item.title" cols="12" sm="4" md="3">
        <CardModule
          :link="item.url"
          :title="item.title"
          :icon="item.icon"
        ></CardModule>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src
import CardModule from "@/components/CardModule.vue";
import {
  mdiAccount,
  mdiBookOpenVariant,
  mdiSemanticWeb,
  mdiCash,
  mdiCurrencyUsd,
  mdiAccountGroup,
  mdiFolderOpen,
  mdiClipboardText,
  mdiLoginVariant,
} from "@mdi/js";

export default {
  name: "Inventory",
  components: {
    CardModule,
  },
  data() {
    return {
      items: [
        { title: "Supplier", url: "/", icon: mdiAccount },
        {
          title: "Customer / Ledgers",
          url: "/Home",
          icon: mdiBookOpenVariant,
        },
        { title: "Products", url: "/Home", icon: mdiSemanticWeb },
        { title: "Expense", url: "/Home", icon: mdiCash },
        { title: "Sales", url: "/Home", icon: mdiCurrencyUsd },
        { title: "Employees", url: "/Home", icon: mdiAccountGroup },
        { title: "Feedback", url: "/Home", icon: mdiFolderOpen },
        { title: "Reports", url: "/Home", icon: mdiClipboardText },
        { title: "Logs", url: "/Home", icon: mdiLoginVariant },
      ],
    };
  },
};
</script>

<style lang="css">
.v-card__title {
  font-size: 20pt;
}
</style>
