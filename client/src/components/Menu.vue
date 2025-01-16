<template>
  <v-data-table
    :headers="headers"
    :items="users"
    density="compact"
    item-key="name"
  >
    <template #top>
      <v-toolbar flat>
        <v-toolbar-title>My CRUD</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        />
        <v-spacer />
        <v-btn @click="createItem()">
          New Item
        </v-btn>
      </v-toolbar>
    </template>
    <template #[`item.username`]="{ item }">
      <p
        style="text-decoration: underline; cursor: pointer"
        @click="redirectToUser(item)"
      >
        {{ item.username }}
      </p>
    </template>
    <template #[`item.actions`]="{ item }">
      <v-icon
        class="me-2"
        size="small"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        size="small"
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
  </v-data-table>
  <Delete
    v-model:dialog-delete="dialogDelete"
    @delete-confirm="deleteItemConfirm"
    @update:dialog-delete="dialogDelete = $event"
  />
  <Edit
    v-model:user="editedUser"
    v-model:dialog="dialog"
    @update:save="save"
  />
  <Create
    v-model:dialog="dialogCreate"
    @create="create"
  />
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      users: [],
      dialogDelete: false,
      dialogCreate:false,
      editedUser: {},
      originalUser: {},
      dialog: false,
      templateialogCreate: false,
      headers: [
        {
          title: "username",
          align: "start",
          sortable: false,
          key: "username",
        },
        {
          title: "Roles",
          align: "start",
          sortable: false,
          key: "joinedRoles",
        },
        { title: "Is Active?", align: "end", key: "active" },
        { title: "Timezone", align: "end", key: "preferences" },
        { title: "Last Update At", align: "end", key: "update_ts" },
        { title: "Created At", align: "center", key: "created_ts" },
        { title: "Actions", key: "actions", sortable: false },
      ],
    };
  },
  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },
  mounted() {
    this.fetchUsers();
  },
  methods: {
    async fetchUsers() {
      axios.get("http://localhost:8000/users").then((response) => {
        response.data.map((user) => {
          user.joinedRoles = user.roles.join(", ");
        });
        this.users = response.data;
      });
    },
    createItem() {
      this.dialogCreate = true;
    },
    editItem(item) {
      this.editedUser = Object.assign({}, item);
      this.originalUser = item;
      this.dialog = true;
    },
    deleteItem(item) {
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      axios.delete(`http://localhost:8000/users/${this.editedItem.username}`).then(() => {
        this.fetchUsers();
      });
      this.closeDelete();
    },
    close() {
      this.dialog = false;
    },
    closeDelete() {
      this.dialogDelete = false;
    },
    create(user) {
      this.setUserRole(user);
      axios.post("http://localhost:8000/users", { users: [user] }).then(() => {
        this.fetchUsers();
        this.close();
      });
    },
    save() {
      this.setUserRole(this.editedUser);
      axios
        .put(`http://localhost:8000/users/${this.originalUser.username}`, this.editedUser)
        .then(() => {
          this.fetchUsers();
          this.close();
        });
    },
    redirectToUser(item) {
      console.log(item);
      this.$router.push({
        name: "details",
        params: { username: item.username },
        query: {
          active: item.active,
          preferences: item.preferences,
          roles: item.roles,
          created_ts: item.created_ts,
          lastUpdateAt : item.update_ts,
        },
      });
    },
    setUserRole(user) {
      for (const role of user.roles) {
        if (role === "admin") {
          user.is_user_admin = true;
        }
        if (role === "manager") {
          user.is_user_manager = true;
        }
        if (role === "tester") {
          user.is_user_tester = true;
        }
      }
    },
  },
};
</script>
