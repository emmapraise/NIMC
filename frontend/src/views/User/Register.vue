<template>
	<div class="container">
		<b-tabs content-class="mt-3" justified>
			<b-tab title="Name" active>
				<b-row v-for="(item, index) in name_tab" :key="index" class="my-2">
					<b-col sm="3">
						<label :for="item.label">{{ item.name }}</label></b-col
					>
					<b-col sm="9">
						<b-form-input
							:id="item.label"
							:type="item.type"
						></b-form-input></b-col></b-row
			></b-tab>

			<b-tab title="Personal Data"> <h2>Personal Data goes here</h2></b-tab>
		</b-tabs>
	</div>
</template>
<script>
export default {
	name: 'RegisterView',
	data() {
		return {
			name_tab: [
				{
					name: 'Surname',
					label: 'surname',
					type: 'text',
				},
				{
					name: 'First Name',
					label: 'last_name',
					type: 'text',
				},
				{
					name: 'Middle Name',
					label: 'middle_name',
					type: 'text',
				},
			],
		};
	},
};
</script>
