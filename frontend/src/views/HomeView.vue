<template>
	<b-container fluid class="bv-example-row">
		<b-row>
			<b-col>
				<div>
					<b-img
						src="https://picsum.photos/300/150/?image=41"
						fluid-grow
						alt="Fluid-grow image"
					></b-img>
				</div>
			</b-col>
			<b-col>
				<b-button variant="success" size="lg">Sign Up</b-button>
				<b-button variant="success" size="lg">Login</b-button>
				<b-button variant="success" size="lg">Check In</b-button>
			</b-col>
		</b-row>
		<!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
	</b-container>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue';

export default {
	name: 'HomeView',
	components: {
		// HelloWorld,
	},
	data() {
		return {
			text: 'this is it',
		};
	},
};
</script>
