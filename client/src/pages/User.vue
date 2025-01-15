<template>
  <div class="user-details">
    <h1>User Details</h1>
    <ul>
      <li><strong>ID:</strong> {{ user.id }}</li>
      <li><strong>Name:</strong> {{ user.name }}</li>
      <li><strong>Email:</strong> {{ user.email }}</li>
      <li><strong>Username:</strong> {{ user.username }}</li>
      <li><strong>Phone:</strong> {{ user.phone }}</li>
      <li><strong>Website:</strong> {{ user.website }}</li>
      <li><strong>Company:</strong> {{ user.company.name }}</li>
      <li>
        <strong>Address:</strong> {{ user.address.street }},
        {{ user.address.city }}
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
export default {
  name: "User",
  data() {
    return {
      user: {
        id: 1,
        name: "John Doe",
        email: "john.doe@example.com",
        username: "johndoe",
        phone: "123-456-7890",
        website: "www.johndoe.com",
        company: {
          name: "Doe Enterprises",
        },
        address: {
          street: "123 Main St",
          city: "Anytown",
        },
      },
    };
  },
};
</script>
