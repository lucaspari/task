<template>
  <v-data-table
    :headers="headers"
    :items="users"
    density="compact"
    item-key="name"
  >
    <template v-slot:item.actions="{ item }">
      <v-icon class="me-2" size="small" @click="editItem(item)">
        mdi-pencil
      </v-icon>
      <v-icon size="small"> mdi-delete </v-icon>
    </template>
  </v-data-table>
  <v-dialog v-model="dialog" max-width="500px">
    <v-card>
      <v-card-title class="text-h5">Edit User</v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="6" md="6" sm="6">
              <v-text-field
                v-model="editedUser.username"
                label="username"
              ></v-text-field>
            </v-col>
            <v-col cols="6" md="6" sm="6">
              <v-checkbox
                label="active"
                v-model="editedUser.active"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col cols="12" align="center" md="6" sm="6">
              <v-text-field
                v-model="editedUser.preferences"
                label="timezone"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue-darken-1" variant="text" @click="close">
              Cancel
            </v-btn>
            <v-btn color="blue-darken-1" variant="text" @click="save">
              Save
            </v-btn>
          </v-card-actions>
        </v-container>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
<script lang="ts">
import type { User } from "@/models/User";
import axios from "axios";
export default {
  data() {
    return {
      users: [],
      editedUser: {},
      originalUser: {},
      dialog: false,
      headers: [
        {
          title: "username",
          align: "start" as const,
          sortable: false,
          key: "username",
        },
        {
          title: "Roles",
          align: "start" as const,
          sortable: false,
          key: "joinedRoles",
        },
        { title: "Is Active?", align: "end" as const, key: "active" },
        { title: "Timezone", align: "end" as const, key: "preferences" },
        { title: "Last Update At", align: "end" as const, key: "update_ts" },
        { title: "Created At", align: "center" as const, key: "created_ts" },
        { title: "Actions", key: "actions", sortable: false },
      ],
    };
  },
  watch: {
    dialog(val) {
      val || this.close();
    },
  },
  mounted() {
    this.fetchUsers();
  },
  methods: {
    async fetchUsers() {
      axios.get("http://localhost:8000/users").then((response) => {
        response.data.map((user: User) => {
          user.joinedRoles = user.roles.join(", ");
        });
        this.users = response.data;
      });
    },
    editItem(item: User) {
      this.editedUser = this.users.indexOf(item);
      this.editedUser = Object.assign({}, item);
      this.originalUser = item;
      this.dialog = true;
    },
    close() {
      this.dialog = false;
    },
    save() {
      this.setUserRole(this.editedUser);
      axios
        .put(
          `http://localhost:8000/users/${this.originalUser.username}`,
          this.editedUser
        )
        .then(() => {
          this.fetchUsers();
          this.close();
        });
    },
    setUserRole(user: User) {
      console.log(user);
      for (const role of user.roles) {
        if (role === "admin") {
          this.editedUser.is_user_admin = true;
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
