<template>
	<div class="about">
		<header-vue />
		<h1>This is an about page</h1>
		<v-btn depressed color="primary" x-large> Click me </v-btn>
		<v-btn depressed color="error"> Primary </v-btn>
		<v-alert border="top" color="red lighten-2">
			I'm an alert with a top border and red color
		</v-alert>
		<uploadfile-vue />
	</div>
</template>

<script>
import HeaderVue from '@/components/header/Header.vue';
import uploadfileVue from '@/components/file/uploadfile.vue';
export default {
	name: 'AboutView',
	components: { uploadfileVue, HeaderVue },
};
</script>
