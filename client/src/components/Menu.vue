<template>
  <v-data-table
    :headers="headers"
    :items="users"
    density="compact"
    item-key="name"
  ></v-data-table>
</template>
<script lang="ts">
import axios from "axios";
export default {
  data() {
    return {
      users: [],
      headers: [
        { title: "username", align: "start", sortable: false, key: "username" },
        { title: "Roles", align: "start", sortable: false, key: "roles" },
        { title: "Is Active?", align: "end", key: "active" },
        { title: "Timezone", align: "end", key: "preferences" },
        { title: "Last Update At", align: "end", key: "update_ts" },
        { title: "Created At", align: "end", key: "created_ts" },
      ],
    };
  },
  mounted() {
    this.fetchUsers();
  },
  methods: {
    async fetchUsers() {
      axios.get("http://localhost:8000/users").then((response) => {
        response.data.map((user) => {
          user.roles = user.roles.join(", ");
        });
        this.users = response.data;
      });
    },
  },
};
</script>
