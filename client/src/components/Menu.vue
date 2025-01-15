<template>
  <v-data-table
    :headers="headers"
    :items="users"
    density="compact"
    item-key="name"
  >
    <template #top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>My CRUD</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        />
        <v-spacer />
        <v-btn>New Item</v-btn>
      </v-toolbar>
      <v-dialog
        v-model="dialogCreate"
        max-width="500px"
      >
        <v-card>
          <v-card-title class="text-h5">
            Create User
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="6"
                  md="6"
                  sm="6"
                >
                  <v-text-field
                    v-model="editedUser.username"
                    label="username"
                  />
                </v-col>
                <v-col
                  cols="6"
                  md="6"
                  sm="6"
                >
                  <v-checkbox
                    v-model="editedUser.active"
                    label="active"
                  />
                </v-col>
              </v-row>
              <v-row
                align="center"
                justify="center"
              >
                <v-col
                  cols="12"
                  align="center"
                  md="6"
                  sm="6"
                >
                  <v-text-field
                    v-model="editedUser.preferences"
                    label="timezone"
                  />
                </v-col>
              </v-row>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="blue-darken-1"
                  variant="text"
                  @click="close"
                >
                  Cancel
                </v-btn>
                <v-btn
                  color="blue-darken-1"
                  variant="text"
                  @click="save"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-container>
          </v-card-text>
        </v-card>
      </v-dialog>
    </template>
    <template #[`item.username`]="{ item }">
      <a @click="redirectToUser(item)">{{ item.username }}</a>
    </template>
    <template #[`item.actions`]="{ item }">
      <v-icon
        class="me-2"
        size="small"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon @click="deleteItem(item)" size="small">
        mdi-delete
      </v-icon>
    </template>
  </v-data-table>
  <v-dialog
    v-model="dialog"
    max-width="500px"
  >
    <v-card>
      <v-card-title class="text-h5">
        Edit User
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col
              cols="6"
              md="6"
              sm="6"
            >
              <v-text-field
                v-model="editedUser.username"
                label="username"
              />
            </v-col>
            <v-col
              cols="6"
              md="6"
              sm="6"
            >
              <v-checkbox
                v-model="editedUser.active"
                label="active"
              />
            </v-col>
          </v-row>
          <v-row
            align="center"
            justify="center"
          >
            <v-col
              cols="12"
              align="center"
              md="6"
              sm="6"
            >
              <v-text-field
                v-model="editedUser.preferences"
                label="timezone"
              />
            </v-col>
          </v-row>
          <v-card-actions>
            <v-spacer />
            <v-btn
              color="blue-darken-1"
              variant="text"
              @click="close"
            >
              Cancel
            </v-btn>
            <v-btn
              color="blue-darken-1"
              variant="text"
              @click="save"
            >
              Save
            </v-btn>
          </v-card-actions>
        </v-container>
      </v-card-text>
    </v-card>
  </v-dialog>
  <v-dialog
    v-model="dialogDelete"
    max-width="500px"
  >
    <v-card>
      <v-card-title class="text-h5">
        Are you sure you want to delete this item?
      </v-card-title>
      <v-card-actions>
        <v-spacer />
        <v-btn
          color="blue-darken-1"
          variant="text"
          @click="closeDelete"
        >
          Cancel
        </v-btn>
        <v-btn
          color="blue-darken-1"
          variant="text"
          @click="deleteItemConfirm"
        >
          OK
        </v-btn>
        <v-spacer />
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      users: [],
      dialogDelete: false,
      editedUser: {},
      originalUser: {},
      dialog: false,
      dialogCreate:false,
      headers: [
        {
          title: "username",
          align: "start" ,
          sortable: false,
          key: "username",
        },
        {
          title: "Roles",
          align: "start" ,
          sortable: false,
          key: "joinedRoles",
        },
        { title: "Is Active?", align: "end" , key: "active" },
        { title: "Timezone", align: "end" , key: "preferences" },
        { title: "Last Update At", align: "end" , key: "update_ts" },
        { title: "Created At", align: "center" , key: "created_ts" },
        { title: "Actions", key: "actions", sortable: false },
      ],
    };
  },
  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete (val) {
        val || this.closeDelete()
      },
  },
  mounted() {
    this.fetchUsers();
  },
  methods: {
    async fetchUsers() {
      axios.get("http://localhost:8000/users").then((response) => {
        response.data.map((user ) => {
          user.joinedRoles = user.roles.join(", ");
        });
        this.users = response.data;
      });
    },
    editItem(item) {
      this.editedUser = Object.assign({}, item);
      this.originalUser = item;
      this.dialog = true;
    },
    deleteItem (item) {
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        axios
          .delete(`http://localhost:8000/users/${this.editedItem.username}`)
          .then(() => {
            this.fetchUsers();
          });
        this.closeDelete()
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
        .put(
          `http://localhost:8000/users/${this.originalUser.username}`,
          this.editedUser
        )
        .then(() => {
          this.fetchUsers();
          this.close();
        });
    },
    redirectToUser(item ) {
      this.$router.push({
        name: "details",
        params: { username: item.username },
        query: { active: item.active, preferences: item.preferences},
      });
    },
    setUserRole(user ) {
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
