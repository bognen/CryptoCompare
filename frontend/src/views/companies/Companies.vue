<template>
    <div class="main-div">
        <section class="generic-banner relative">
            <div class="container">
                <div class="row height align-items-center justify-content-center">
                    <div class="col-lg-10">
                        <div class="generic-banner-content">
                            <h2 class="text-white">The Generic Page</h2>
                            <p class="text-white">It won’t be a bigger problem to find one video game lover in your <br> neighbor. Since the introduction of Virtual Game.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <ul>
          <li v-for="post in posts" :key="post.id">{{post.title}}</li>
        </ul>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "Companies",
        data() {
            return {
                posts: [],
                errors: []
            }
        },

        // Fetches posts when the component is created.
        created() {
            axios.get(`http://jsonplaceholder.typicode.com/posts`)
                .then(response => {
                    // JSON responses are automatically parsed.
                    this.posts = response.data
                })
                .catch(e => {
                    this.errors.push(e)
                })
        }
    }
</script>

<style scoped>

</style>