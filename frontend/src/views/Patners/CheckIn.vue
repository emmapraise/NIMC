<template>
	<div class="container">
		<div class="mx-auto w-25">
			<b-input-group class="mb-2 mt-2">
				<b-input-group-prepend is-text>
					<b-icon icon="person-fill"></b-icon>
				</b-input-group-prepend>
				<b-form-input type="text" placeholder="Enter NIN"></b-form-input>
			</b-input-group>

			<b-input-group class="mb-2 mt-2">
				<b-input-group-prepend is-text>
					<b-icon icon="upc-scan"></b-icon>
				</b-input-group-prepend>
				<b-form-input
					type="password"
					placeholder="Enter Passcode"
				></b-form-input>
			</b-input-group>

			<b-button variant="success" block class="mt-3">Check In</b-button>
		</div>
	</div>
</template>
