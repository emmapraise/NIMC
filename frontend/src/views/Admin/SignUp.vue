<template>
	<div class="container">
		<div class="mx-auto w-25">
			<b-input-group class="mb-2 mt-2">
				<b-input-group-prepend is-text>
					<b-icon icon="person-fill"></b-icon>
				</b-input-group-prepend>
				<b-form-input type="text" placeholder="Enter Username"></b-form-input>
			</b-input-group>

			<b-input-group class="mb-2 mt-2">
				<b-input-group-prepend is-text>
					<b-icon icon="envelope-fill"></b-icon>
				</b-input-group-prepend>
				<b-form-input
					type="email"
					placeholder="Enter email address"
				></b-form-input>
			</b-input-group>

			<b-input-group class="mb-2 mt-2">
				<b-input-group-prepend is-text>
					<b-icon icon="telephone-fill"></b-icon>
				</b-input-group-prepend>
				<b-form-input
					type="tel"
					placeholder="Enter Phone Number"
				></b-form-input>
			</b-input-group>

			<b-input-group class="mb-2 mt-2">
				<b-input-group-prepend is-text>
					<b-icon icon="lock-fill"></b-icon>
				</b-input-group-prepend>
				<b-form-input
					type="password"
					placeholder="Enter Password"
				></b-form-input>
			</b-input-group>

			<b-button variant="success" block class="mt-3">Sign Up</b-button>
		</div>
	</div>
</template>
<script> 
export default {
	name: "SignUp"
}
</script>
