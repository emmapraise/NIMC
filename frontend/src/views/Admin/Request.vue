<template>
	<div>
		<header-vue :logout="true" />
		<b-row class="mt-2">
			<b-col md="2">
				<sidebar-vue />
			</b-col>
			<b-col md="10">
				<b-card title="Update Requests" class="">
					<b-table
						:items="items"
						:fields="fields"
						responsive="md"
						sticky-header
						head-variant="info"
						class="mt-2"
					>
						<template #cell(index)="row">
							{{ row.index + 1 }}
						</template>
						<template #cell(actions)>
							<b-icon
								icon="check"
								v-b-tooltip.hover.top="'Approve'"
								font-scale="1.5"
								role="button"
							/>
							<b-icon
								icon="x"
								v-b-tooltip.hover.top="'Cancel'"
								font-scale="1.5"
								role="button"
							/>
							<b-icon
								icon="eye"
								v-b-tooltip.hover.top="'View'"
								font-scale="1.5"
								role="button"
							/>
						</template>
					</b-table>
				</b-card>
			</b-col>
		</b-row>
	</div>
</template>
<script>
import HeaderVue from '@/components/header/Header.vue';
import SidebarVue from '@/components/sidebar/Sidebar.vue';
export default {
	name: 'RequestsView',
	components: {
		HeaderVue,
		SidebarVue,
	},
	data() {
		return {
			data: {},
			fields: [
				{ key: 'index', sortable: true },
				{ key: 'last_name', sortable: true },
				{ key: 'first_name', sortable: true },
				{ key: 'age', sortable: true },
				{ key: 'isActive', sortable: false },
				{ key: 'actions', sortable: false },
			],
			items: [
				{
					isActive: true,
					age: 40,
					first_name: 'Dickerson',
					last_name: 'Macdonald',
				},
				{ isActive: false, age: 21, first_name: 'Larsen', last_name: 'Shaw' },
				{ isActive: false, age: 89, first_name: 'Geneva', last_name: 'Wilson' },
				{ isActive: true, age: 38, first_name: 'Jami', last_name: 'Carney' },
			],
		};
	},
};
</script>
