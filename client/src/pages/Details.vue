<template>
  <v-container
    class="d-flex justify-center align-center"
    style="height: 100vh"
  >
    <v-card class="pa-5">
      <v-card-title>User Details</v-card-title>
      <v-card-text>
        <span><b>Username:</b></span>
        <p>{{ username }}</p>
        <span><b>Active:</b></span>
        <p>{{ active }}</p>
        <span><b>Preferences</b></span>
        <p>{{ preferences }}</p>
        <span><b>Roles</b></span>
        <ul>
          <p
            v-for="role in roles"
            :key="role || ''"
          >
            {{ role }}
          </p>
        </ul>
        <span><b>Created At</b></span>
        <p>{{ created_ts }}</p>
        <span><b>Update At</b></span>
        <p>{{ update_ts }}</p>
      </v-card-text>
      <v-card-actions>
        <v-btn
          color="primary"
          @click="editItem"
        >
          Edit
        </v-btn>
        <v-btn
          color="red"
          @click="deleteItem"
        >
          Delete
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
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
</template>

<script lang="js">
import axios from "axios";

export default {
  name: "User",
  data() {
    return {
      username: this.$route.params.username ,
      active: this.$route.query.active,
      preferences: this.$route.query.preferences,
      created_ts : this.$route.query.created_ts,
      roles : this.$route.query.roles,
      update_ts : this.$route.query.lastUpdateAt
      ,
      editedUser: {} ,
      dialog: false,
      dialogDelete: false,
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
  methods: {
    editItem() {
      this.editedUser = {
        username: this.username,
        active: JSON.parse(this.active) ,
        preferences: String(this.preferences),
        created_ts: String(this.created_ts),
        roles: this.roles ,
      };
      this.dialog = true;
    },
    deleteItem() {
      this.dialogDelete = true;
    },
    close() {
      this.dialog = false;
    },
    closeDelete() {
      this.dialogDelete = false;
    },
    save() {
      this.setUserRole(this.editedUser);
      axios
        .put(`http://localhost:8000/users/${this.username}`, this.editedUser)
        .then(() => {
          this.close();
          this.redirectToHome();
        });
    },
    deleteItemConfirm() {
      axios.delete(`http://localhost:8000/users/${this.username}`).then(() => {
      });
      this.closeDelete();
      this.redirectToHome();
    },
    setUserRole(user) {
      if(user.roles === undefined) {
        return;
      }
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
    redirectToHome() {
      this.$router.push({
        path: "/",
      });
    },
  },
};
</script>
