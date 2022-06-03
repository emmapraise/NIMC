<template>
	<div class="container">
		<div
			class="row justify-content-center align-items-center main mx-auto mt-5"
		>
			<div class="col-md-4" role="button" @click="handleClick('login')">
				<div class="card">
					<div class="d-flex flex-column align-items-center w-100 p-5">
						<b-icon icon="person-fill"></b-icon>
						<span style="font-weight: bold; width: fit-content"
							>User Login</span
						>
						<span class="text-secondary"> User Login to Dashboard </span>
					</div>
				</div>
			</div>

			<div
				class="col-md-4"
				role="button"
				@click="handleClick('admin/register')"
			>
				<div class="card">
					<div class="d-flex flex-column align-items-center w-100 p-5">
						<b-icon icon="person-plus-fill" aria-hidden="true"></b-icon>
						<span style="font-weight: bold; width: fit-content">Sign Up</span>
						<span class="text-secondary">Login or Sign up a new Admin</span>
					</div>
				</div>
			</div>

			<div
				class="col-md-4"
				role="button"
				@click="handleClick('patners/checkin')"
			>
				<div class="card">
					<div class="d-flex flex-column align-items-center w-100 p-5">
						<b-icon icon="search" aria-hidden="true"></b-icon>
						<span style="font-weight: bold; width: fit-content">Check In</span>
						<span class="text-secondary">Check the Validity of a NIN</span>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'HomeView',
	components: {},
	data() {
		return {
			text: 'this is it',
		};
	},
	methods: {
		handleClick(route) {
			this.$router.push(route);
		},
	},
};
</script>
