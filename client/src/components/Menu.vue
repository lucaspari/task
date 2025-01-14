<template>
  <v-data-table
    :headers="headers"
    :items="users"
    :items-per-page="5"
    class="elevation-1"
    :footer-props="{
      'items-per-page-options': [5, 10, 15],
    }"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Users</v-toolbar-title>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-btn class="mr-2" color="primary">Edit</v-btn>
      <v-btn color="error">Delete</v-btn>
    </template>
  </v-data-table>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      users: [],
      headers: [
        { text: "Username", value: "username" },
        { text: "Timezone", value: "preferences" },
        { text: "Is Active?", value: "active" },
        { text: "Last Update At", value: "update_ts" },
        { text: "Created At", value: "created_ts" },
        { text: "Actions", value: "actions", sortable: false },
      ],
    };
  },
  mounted() {
    this.fetchUsers();
  },
  methods: {
    async fetchUsers() {
      axios.get("http://localhost:8000/users").then((response) => {
        console.log(response.data);
        this.users = response.data;
      });
    },
  },
});
</script>
